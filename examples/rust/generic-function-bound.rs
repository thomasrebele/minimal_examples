#![allow(dead_code)]
#![allow(unused_variables)]

//x description="generic function with bounds"


struct ICE {
    power: f32,
}

//x pre={
trait Train {
    fn acceleration(&self, speed: f32) -> f32;
}

impl Train for ICE {
    // ...
//x }
    fn acceleration(&self, speed: f32) -> f32 {
        return self.power / speed;
    }
}

//x pre={
fn init_accel(train : &Train) -> f32 {
    train.acceleration(0.)
}

// task: take train by value
//x }

//x step={
fn init_accel_generic<W : Train>(train : W) -> f32 {
    train.acceleration(0.)
}
//x }


//x explanation="'train : Train' breaks compilation: `Train + 'static` does not have a constant size known at compile-time"


fn main() {
//x post={
let ice = ICE{power: 10.};
init_accel(&ice);
init_accel_generic(ice);
//x }
}

