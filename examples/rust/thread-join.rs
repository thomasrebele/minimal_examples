
fn main() {

//x description="wait for thread"
//x level=15

//x pre={
let t = std::thread::spawn(
    || println!("executed by thread")
);
// wait for thread to finish
//x }

//x step={
let _ = t.join();
//x }

}
