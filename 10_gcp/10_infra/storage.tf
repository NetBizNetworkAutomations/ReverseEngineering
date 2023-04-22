resource "google_storage_bucket" "tfstate-storage" {
  name          = "tfstate-bucket-dts-training-2021"
  location      = "asia-northeast1"
  
  force_destroy = true
  uniform_bucket_level_access = true
}