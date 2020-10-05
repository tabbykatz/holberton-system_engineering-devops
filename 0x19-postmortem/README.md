# Postmortem

## How I Destroyed 3 Servers, Rebuilt Them, and Destroyed Them Again the Next Day

![An image of the command line where repeated ssh attempts result in “port 22: connection refused.”](https://miro.medium.com/max/2104/1*aNsuz7CGA7AGQ9LdjY4xlA.png)

This is what we were warned about.

# Issue Summary

I was issued 3 servers at midnight PST on August 14th, 2020 as part of my DevOps training, and directed to configure them as specified. Afterwards, I neglected to preserve my rsa private key upon replacing my laptop, killing all 3 servers. Lessons learned, the rebuild occurred on Sept 30th. During the rebuild I took extensive notes.

On the morning of October 1st, 2020, I destroyed web-01, apparently by locking port 22.

The issue was noticed upon reboot. All attempts to ssh back in failed.

The rebuild went well the day before, and the servers were all functioning as expected that morning. `ufw` rules were all perfectly set. The final commands I gave to web-01 were:

    $ sudo hostnamectl set-hostname 1346-web-01  
    $ sudo vim /etc/hosts [replacing old hostname manually with 1346-web-01 to make it persistent]  
    $ sudo reboot

# Timeline

![Image depicting timeline of events](https://miro.medium.com/max/4300/1*OytaPdQPJlcdWL6OgTG4eQ.png)
How can I blame this on 2020?

Timeline of the events of October 1st, 2020:

-   Thu Oct 1 08:48 — successfully logged into all servers from my VM
-   Thu Oct 1 09:15 — it was brought to my attention that I forgot to set persistent hostnames during the rebuild, so I did so following [this tutorial](https://www.cyberciti.biz/faq/ubuntu-18-04-lts-change-hostname-permanently/), beginning with web-01, using what turned out to be my final commands to the server.
-   Thu Oct 1 09:50 — cannot ssh back into web-01, alert SWE in residence Kristen Loyd.
-   Thu Oct 1 09:55 — attempt to ssh back in after both soft and hard reboot.
-   Thu Oct 1 10:00 — many hours of research ranging from admin access to white hat breaking ufw.
-   Thu Oct 1 16:16 — Our CTO Guillaume Salva suggests he can get back in, gives it his best shot, but declares the server dead.

----------

-   Sun 0ct 4 14:20 — I request a new server, satisfied that I have exhausted all possibilities for repair.

# Root cause and resolution

I am certain that my ufw rules were perfectly in place:

    sudo ufw enable  
    sudo ufw status verbose  
    sudo ufw default deny incoming  
    sudo ufw default allow outgoing  
    sudo ufw allow 22/tcp  
    sudo ufw allow 443/tcp  
    sudo ufw allow 80/tcp  
    sudo ufw enable  
    sudo ufw status  
    sudo ufw allow 8080/tcp  
    sudo vim /etc/ufw/before.rules  
    sudo ufw enable   
    sudo ufw status

I had taken thorough notes while rebuilding these servers, and logged back in as expected on the day in question. While inspecting web-02 after the event, I could see that ufw was working on the twin server.

Because there was no happy resolution to this issue, I surmise that using the command `sudo reboot` somehow reset my ufw rules, although I am baffled that ufw would be changed from the rules above to block port 22 by a simple reboot.

The ultimate “fix” was requesting new server, which I did just now.

![Image for post](https://miro.medium.com/max/1156/1*Bf2aYwg9YvEen26rK8RDig.png)

Third time’s the charm?

# Corrective and preventative measures

Without a clear understanding of the cause of this event, I cannot be sure of the best course of action to prevent its like again. What I know for certain is that until I do understand what happened, I will never trust ufw.

However, there is work to be done now that I have requested a new server. it differs from the work of rebuilding all three servers but is not _less work_.

-   fix ssh configuration in my VM so that I can get into the new web-01 easily.
-   set up web-01 so that nginx is properly installed, and add key for staff access.
-   Set persistent hostname
-   fix my domain A records to reflect the new web-01
-   Add custom response header
-   Fix load balancer to reflect these changes
-   Re-certbot
-   Do not at any point in this process use ufw
-   Fix datadog monitoring for the setup

# Takeaways

I have learned a lot from these fiascos. My private key is now protected and saved in LastPass, for example. But the unresolved ufw reboot problem has taught me little. For now, I will keep ufw disabled until I have completed the server-oriented projects from my school.


