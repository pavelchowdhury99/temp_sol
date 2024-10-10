class KeyValueStore {
  private var store: Map[String, String] = Map()

  def put(key: String, value: String): Unit = {
    store = store + (key -> value) // Add or update the value associated with the key
  }

  def get(key: String): Option[String] = {
    store.get(key) // Retrieve the value associated with the key
  }

  def remove(key: String): Unit = {
    store = store - key // Remove the key-value pair from the store
  }

  def keys(): List[String] = {
    store.keys.toList // Return a list of all keys
  }
}