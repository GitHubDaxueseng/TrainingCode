/**
   * 1. Load:  Read the file textFile
   * 2. Filter :  Filter the data of "status": 0} filter
   * 3. FlatMap:  Convert "data":Array[5] into multiple lines by 'flatMap'
   * 4. Reduce:  Get "school": "XX University", "plan": "x",   by 'reduce'
   * 5. Sort:  Sort the number of schools and enrolled students,
   *           sorted by the number of students enrolled.
   *
   *   Created by Google on 7/23/2018.
  */
import org.json.JSONObject
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext
import scala.collection.mutable.ListBuffer
object Statistics{
  def main(args: Array[String]){
    val conf = new SparkConf().setAppName("calcu").setMaster("local")
    //Loading configurations
    val sc = new SparkContext(conf)
    //Loading data
    sc.textFile("E:\\云南_西藏_陕西.txt")
    //Filter the valuable data
    //status":1
    .filter(line => line.endsWith("status\":1}"))
    //Flat the data
      .flatMap(line => {
      //Translate line into json data
      val json = new JSONObject(line)
      //Get the array in json which named 'data'
      val jsonList = json.getJSONArray("data")
      val list = ListBuffer[JSONObject]()
      for(i <- 0 to jsonList.length() - 1){
        list.append(jsonList.getJSONObject(i))
      }
      list
    })
      .map(line => (line.getString("school"),line.getString("plan").toInt))
      .reduceByKey(_+_)
      .foreach(line => println(line))
  }}

