

//x step={
fn head(slice: &[i32]) {
    println!("first {} len {}", slice[0], slice.len());   
}
//x }

fn main() {

//x description="boolean variable"
//x step={
    let _a = [0,1,2,3,4];
    
    head(&_a);
    // slice with content [2,3]
    head(&_a[2..4]); 
//x }

}
