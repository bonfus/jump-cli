# jump-cli

> The most secure system is one that nobody can use!

Running high-throughput simulations on HPC clusters requires uninterrupted access to the login nodes of the target machine, but the 2FA authentication methods generating very short lived keys makes it almost impossible to perform this kind of activity.

`jump-cli` is just a few lines of code that automate the generation of ssh keys with `step-cli`. It stores all your credentials in a password protected configuration file and uses them to generate a new ssh-key with `step-cli` every two hours. The code is as small as possible so that you can easily adapt it to your needs. It currently targets Linux but can be easily ported to other OSes.

## Configuration

Just run

```bash
python ./gen_config.py
```

and insert your credentials. A password 

## Usage

Just pass the same options that you use for step-cli, for example:

```bash
    ./jump-cli ssh certificate "your-user" --force --insecure --no-password --no-agent --provisioner your-prov ~./ssh/your-shiny-new-keys
```

`jump-cli` will start a never ending loop to update you keys every 2 hours.

## Security

Obviously this approach defeats 2FA, and the confidentiality of your credentials is only secured by the password encrypted configuration file. This is basically the same as having a password protected key file, with the inconvenience that your credentials may also give access to other services. This is not at all advisable, but it's unfortunately the only possibility for running high-throughput simulations on the HPC platforms that I can access for the time being.



