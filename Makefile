create:
	aws cloudformation create-stack --stack-name cloudguardrail --template-body ./template.yaml --capabilities CAPABILITY_IAM
validate:
	aws cloudformation validate-template --template-body ./template.yaml
