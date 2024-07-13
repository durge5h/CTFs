
.......................................Linux.......................................
- If you do not want to run out of protection (unspecified developer) (Ubuntu):
1) Right-click on the file, go to "Properties."
2) Go to the "Permissions" tab and check the box next to "Enable file execution as a program".

- If the launcher did not start or an error occurred:
1) Install Java: sudo apt-get install openjdk-8-jre
2) After install JavaFX: sudo apt-get install openjfx
(If you have Java 9 or 10, you need to install Java 8 and get the launcher to work from it,
or completely remove Java 9 or 10.)

- Important! We recommend that you run with root if you run without root privileges,
then there are problems with the graphics (gpu).
Run as follows:
1) Navigate to the client folder using the CD command
2) Running: sudo java -jar TLauncher.jar
.......................................Arch Linux.......................................
1) Update your system: sudo pacman -Suuy
2) Install packets: sudo pacman -S java8-openjfx jdk8-openjdk jre8-openjdk jre8-openjdk-headless
.......................................Debian/Mint.......................................
1) Update your system: sudo apt-get update , and then "sudo apt-get upgrade" .
2) Install packets: sudo apt install default-jdk
.......................................Fedora/CentOS.......................................
1) Update your system: sudo yum update
2) Install packets: sudo yum install java-11-openjdk
3) Execute the command: "sudo update-alternatives --config java" and indicate in the field the number of the corresponding version of Java 11 to set it as default.
.......................................MacOS.......................................
- If he does not want to run due to protection (unidentified developer): 
1) Open "Settings" and go to "Security" (General tab).
2) Click on "Confirm open". The launcher will open!

- If the launcher did not start or an error occurred:
1) Install Java again by downloading the installer from the official site https://java.com/
(If you have Java 9 or 10, you need to install Java 8 and get the launcher to work from it,
or completely remove Java 9 or 10.)
