/**
  * Created by Google on 7/20/2018.
  */
object Scala2 {
  def main(args: Array[String]) {
    val ls = List(25,21,28,39,45,51,25)
    for(i <- ls){
      if(i == 28){
        print("Wednesday:")
      }else{
        println(i)
      }
    }
  }
}
