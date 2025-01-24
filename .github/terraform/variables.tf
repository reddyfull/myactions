variable "bucket_name" {
    description = "The name of the S3 bucket"
    type        = string
    default     = "my-default-bucket"
}
variable "bucket_region" {
  description = "Region for the S3 bucket"
  type        = string
  default     = "us-west-2"
}
