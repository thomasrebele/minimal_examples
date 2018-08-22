#[allow(unused_variables)]
#[allow(unused_mut)]


//x description="define a unit test"

//x step={
#[test]
//x }
//x post={
fn add() {
    assert_eq!(1+1, 2);
    // tests ignore println
}
//x }

fn main() {
    println!("compile with --test");
}
