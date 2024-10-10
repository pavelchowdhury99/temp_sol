import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class KeyValueStoreSpec extends AnyFlatSpec with Matchers {

  "A KeyValueStore" should "allow adding and updating key-value pairs" in {
    val kvStore = new KeyValueStore
    kvStore.put("key1", "value1")
    kvStore.get("key1") should be(Some("value1"))

    kvStore.put("key1", "value2")
    kvStore.get("key1") should be(Some("value2"))
  }

  it should "return None for a non-existent key" in {
    val kvStore = new KeyValueStore
    kvStore.get("nonExistentKey") should be(None)
  }

  it should "allow removing key-value pairs" in {
    val kvStore = new KeyValueStore
    kvStore.put("key1", "value1")
    kvStore.remove("key1")
    kvStore.get("key1") should be(None)
  }

  it should "not throw an error when removing a non-existent key" in {
    val kvStore = new KeyValueStore
    kvStore.remove("nonExistentKey") // Should not throw an error
  }

  it should "return a list of all keys" in {
    val kvStore = new KeyValueStore
    kvStore.put("key1", "value1")
    kvStore.put("key2", "value2")
    kvStore.keys() should contain allOf ("key1", "key2")
    kvStore.keys().length should be(2)
  }

  it should "return an empty list when no keys exist" in {
    val kvStore = new KeyValueStore
    kvStore.keys() should be(empty)
  }
}
