
#![allow(unused_variables)]

//x pre={

//x }

fn main() {

//x description="access component in match"

//x pre={

let a = Some("alice".to_string());

match a {
    Some(n) => (),
    _ => (),
}

// println!("a {:?}", a); 
//   error: use of partially moved value

// how to print name without destroying a ?
//x }

let a = Some("alice".to_string());
//x step={
match a {
    Some(ref n) => (),
    _ => (),
}

println!("a {:?}", a);
//x }

}

