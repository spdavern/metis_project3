# AWS Database Connection

Starting the AWS machine instance: (See [1] for setup instructions )

1. Sign into the [AWS console](https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin).
2. Go to the [EC2 service](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2). Under Instances is [Instances](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Instances:).  Start the machine instance of interest. (Select instance > Actions button > Instance State > Start)
3. Get the IPv4 Public IP address that was assigned to the, now running, instance.  In this case it was now: 34.219.19.96
4. Open a terminal window (zsh) and ssh into the remote machine:
   1. Log onto your AWS instance using

```bash
# standard way
ssh -i ~/.ssh/aws_key.pem ubuntu@<your ip address>
# using config file  (NOTE: Config file must be upto date.)
ssh ubuntu@myaws
```

​		The config file method works because I modified `~/.ssh/config` to include

```Host myaws
HostName 18.216.164.22 # use your IP instead
        User ubuntu
        IdentityFile ~/.ssh/aws_key.pem
```

​		To edit the config file do: `nano ~/.ssh/config`, edit the IP address and save.

​		2.	You should now have a cursor like: 

​					`(base) ubuntu@ip-172-31-17-117:~$`

​				showing the ip address from where you're connecting from.

5. You should now be able to do all variety of ubuntu commands including

   `psql`

6. To exit from ubuntu machine use `exit` to which you should get:

   ```logout
   logout
   Connection to 34.219.19.96 closed.
   (base) sean@Seans-MacBook-Pro SQL Challenges %
   ```

[^1]: Instructions for setting up the ubuntu instance: sea19_ds10/curriculum/project-03/aws-setup/00_setup_aws_ec2.md

