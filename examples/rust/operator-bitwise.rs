
fn main() {

//x description="logical operators"
//x code={
    let a = 0b0011u32;
    let b = 0b0101u32;

    // print bits, padded with zeros
    println!("0011 and 0101: {:04b}", a & b);
    println!("0011  or 0101: {:04b}", a | b);
    println!("0011 xor 0101: {:04b}", a ^ b);
//x }

}
