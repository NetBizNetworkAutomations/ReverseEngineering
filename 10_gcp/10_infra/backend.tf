terraform {
 backend "gcs" {
   bucket  = "tfstate-bucket-dts-training-2021"
   prefix  = "terraform/state"
 }
}