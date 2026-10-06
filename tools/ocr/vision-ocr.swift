// Apple Vision text recognition for pinout images (macOS only, no network).
// Usage: vision-ocr <image>...  → one JSON object per line:
// {"file": path, "width": px, "height": px, "lines": [{"text": s, "confidence": c, "box": [x, y, w, h]}]}
// Boxes are in pixels with the origin at the top-left of the image.
import Foundation
import Vision
import ImageIO

func recognize(_ path: String) -> [String: Any] {
    guard let source = CGImageSourceCreateWithURL(URL(fileURLWithPath: path) as CFURL, nil),
          let image = CGImageSourceCreateImageAtIndex(source, 0, nil) else { return ["file": path, "error": "unreadable image"] }
    let width = Double(image.width), height = Double(image.height)
    var lines: [[String: Any]] = []
    let request = VNRecognizeTextRequest { request, _ in
        for observation in (request.results as? [VNRecognizedTextObservation]) ?? [] {
            guard let best = observation.topCandidates(1).first else { continue }
            let b = observation.boundingBox
            lines.append(["text": best.string, "confidence": Double(best.confidence),
                          "box": [b.minX * width, (1 - b.maxY) * height, b.width * width, b.height * height]])
        }
    }
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = false   // pin names are not dictionary words
    request.minimumTextHeight = 0.004        // pinout labels are small relative to the artwork
    do { try VNImageRequestHandler(cgImage: image, options: [:]).perform([request]) }
    catch { return ["file": path, "error": "\(error)"] }
    return ["file": path, "width": width, "height": height, "lines": lines]
}

for path in CommandLine.arguments.dropFirst() {
    let data = try! JSONSerialization.data(withJSONObject: recognize(path), options: [])
    print(String(data: data, encoding: .utf8)!)
}
