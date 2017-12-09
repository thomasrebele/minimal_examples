#![allow(unused_variables)]

fn main() {

//x description="use a channel"
//x level=20

//x pre={
use std::sync::mpsc::*;
let (s, r) : (Sender<i32>, Receiver<i32>) = channel();
//x }

//x step={
std::thread::spawn(
    move || s.send(1)
    // send does not block
);

let a = r.recv();
//x }

}
