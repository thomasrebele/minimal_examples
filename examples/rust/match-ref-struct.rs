
#![allow(unused_variables)]

#[derive(Debug)]
//x pre={
enum Entry {
    Name{n : String}
}
//x }

fn main() {

//x description="access field in match"

//x pre={
use Entry::*;

let a = Name{n : "alice".to_string()};

match a {
    Name{n} => (),
}

// println!("a {:?}", a); 
//   error: use of partially moved value

// how to print name without destroying a ?
//x }

let a = Name{n : "alice".to_string()};
//x step={
match a {
    Name{ref n} => (),
}

println!("a {:?}", a);
//x }

}

