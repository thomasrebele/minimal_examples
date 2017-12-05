#![allow(unreachable_code)]
#![allow(dead_code)]

fn main() {

fn dummy() {

//x description="break outer loop"
//x pre={
loop {
    loop {
        // get out of both loops!
    }
}
//x }

//x step={
'outer: loop {
    loop {
        break 'outer;
    }
}
//x }

}

}
