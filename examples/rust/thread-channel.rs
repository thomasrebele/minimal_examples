#![allow(unused_variables)]

fn main() {

//x description="define a channel (1)"

//x pre={
use std::sync::mpsc::*;
//x }

//x step={
let (s, r) : (Sender<i32>, Receiver<i32>) = channel();
//x }

//x post={
std::thread::spawn(
    move || s.send(1)
    // send does not block
);

let a = r.recv();
//x }

}
