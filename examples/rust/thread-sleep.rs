
fn main() {

//x description="let thread sleep"
//x level=15

//x pre={
let ten_ms = std::time::Duration::from_millis(10);
//x }

//x step={
std::thread::sleep(ten_ms);
//x }
}
