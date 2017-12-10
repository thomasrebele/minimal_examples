
fn main() {

//x description="execute code in thread"

//x step={
std::thread::spawn(
    || println!("executed by thread")
);
//x }

//x post={
// needs to be executed long enough ...
std::thread::sleep(std::time::Duration::from_millis(100));
//x }

}
