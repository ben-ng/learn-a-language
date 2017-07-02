import scala.io.Source._

val n = args(0).toInt

fromFile("2cities.txt")
  .getLines                                   // Iterator[String] (lazy)
  .flatMap {                                  // Special shorthand syntax for function arguments
    """(?i)[a-z]+"""                          // (?i) Is a Java regex special construct for case-insensitive matching
                    .r                        // .r compiles a Regex from a String
                    .findAllIn(_)             // _ here refers to a line
                    .map {_.toLowerCase}      // _ here refers to a word
  }                                           // Still a lazy Iterator here
  .toSeq                                      // Convert to Sequence so we can groupBy
  .groupBy {identity}                         // `identity` is a predefined function
  .mapValues {_.length}                       // Map[String, List[String]]
  .toSeq                                      // Seq[String -> List[String]] (a->b is a tuple a,b)
  .sortWith {_._2 > _._2}                     // First _ is the arg, the 2nd _ is a tuple getter
  .take(n)                                    // Take the first n in the Seq
  .foreach {case (w, c) => println(s"$c $w")} // `s` makes this a processed string literal for interpolation
 