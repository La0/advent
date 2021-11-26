use std::fs;

// Read file and map to int vector
fn read_integers(path : &str) -> Vec<u32> {
    let content = fs::read_to_string(path)
        .expect("read failure");
    return content.lines().map(|x| x.parse::<u32>().unwrap()).collect();
}

fn main () {
    let ints = read_integers("1.txt"); 
    for (pos, x) in ints.iter().enumerate() {

        for y in &ints[pos+1..] {

            // Part one
            if x + y == 2020 {
                println!("{} + {} = 2020", x, y);
                println!("{} x {} = {}", x, y, x * y);
            }

            // Part two
            for z in ints.iter() {
                if x + y + z == 2020 {
                    println!("{} + {} = 2020", x, y);
                    println!("{} x {} x {} = {}", x, y, z, x * y * z);
                    return;
                }
            }
        }
    }
}
