
public class javadoc_refer_method {

//x description="javadoc: refer to another method"

public static class pre {

//x pre={
/** Does nothing */
public void method(String... param) {
	//...
}

/** See method(String...) */
public void method2() {
	// ...
}
//x }
}

public static class step {
/** Does nothing */
public void method(String... param) {
	//...
}

//x step={
/** See {@link #method(String...)}*/
public void method2() {
//x }
	// ...
}
}


}
