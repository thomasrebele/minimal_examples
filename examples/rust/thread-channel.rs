#![allow(unused_variables)]

fn main() {

//x description="define a channel"

//x step={
use std::sync::mpsc::*;
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
