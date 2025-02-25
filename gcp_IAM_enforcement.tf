resource "google_project_iam_binding" "least_privilege" {
    projct = "project_name"
    role  = "roles/viewer"
    members = [
        "user:email_address"
    ]
}

// install terraform and authenticate GCP:: gcloud auth application-default login
// apply changes: terraform init
//                  terraform -auto-approve