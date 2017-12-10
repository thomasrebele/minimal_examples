
fn main() {

//x description="thread sleep duration"

//x step={
let ten_ms = std::time::Duration::from_millis(10);
//x }

//x pre={
// define ten_ms
std::thread::sleep(ten_ms);
//x }
}
