import boto3

# Create an EC2 client object
ec2 = boto3.client('ec2')

# Initialize an empty list to store instance IDs
ids = []

# Function to retrieve instance IDs
def list_instances():
    # Describe EC2 instances
    response = ec2.describe_instances()
    
    # Iterate over reservations
    for reservation in response['Reservations']:
        # Iterate over instances within each reservation
        for instance in reservation["Instances"]:
            # Append instance ID to the list
            ids.append(instance["InstanceId"])

# Call the list_instances() function to populate the ids list
list_instances()

# Stop each EC2 instance using the instance IDs in the ids list
for compute in ids:
    ec2.stop_instances(InstanceIds=[compute])
