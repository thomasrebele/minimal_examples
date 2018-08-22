
#![allow(unused_variables)]

#[derive(Debug)]
struct Employee {
    id: i32,
    name: String,
    position: String,
    office: String,
    phone: String,
}

fn main() {

//x description="simplify struct in match"

let a = None;
//x pre={
match a {
    Some(Employee{
        id: _,
        name, 
        position: _, 
        office: _,
        phone: _
    }) => println!("{}", name),
    _ => (),
}

// simplify match expression
//x }

let a = Some(Employee{
    id:0,
    name:"alice".to_string(), 
    position:"CEO".to_string(), 
    office:"A007".to_string(),
    phone:"32168".to_string(),
});
//x step={
match a {
    Some(Employee{
        name, 
        ..
    }) => println!("{}", name),
    _ => (),
}
//x }

}

