//setting funky = 1 we have:
import Foundation

let bpm = 70.0
let beatDuration = 60.0 / bpm // seconds per beat

while true {
    print("E = funky*mc**2")
    fflush(stdout)
    Thread.sleep(forTimeInterval: beatDuration)
}
