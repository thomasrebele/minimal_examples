#[allow(unused_variables)]
#[allow(unused_mut)]


//x description="define a test module"

//x step={
#[cfg(test)]
//x }
//x post={
mod tests {

    #[test]
    fn add() {
        assert_eq!(1+1, 2);
        // tests ignore println
    }
}
//x }

fn main() {
    println!("compile with --test");
}
