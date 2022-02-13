package j.ucdavis22.w5;

/*
 * Jörn Boehnke 2022
 */

import java.time.Duration;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

import io.github.bonigarcia.wdm.WebDriverManager;

public class SeleniumDriverManagerTest {

    public static void main(String[] args) throws InterruptedException {
        
        WebDriverManager.chromedriver().setup();
//        WebDriverManager.chromedriver().driverVersion("97.0").setup();
        WebDriver driver = new ChromeDriver();
        
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.manage().timeouts().scriptTimeout(Duration.ofMinutes(2));
        driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(10));
        
        driver.get("https://google.com");
        
        Thread.sleep(1_000);
        
//        driver.findElement(By.className("className"));
//        driver.findElement(By.cssSelector(".className"));
//        driver.findElement(By.id("elementId"));
//        driver.findElement(By.linkText("linkText"));
//        driver.findElement(By.name("elementName"));
//        driver.findElement(By.partialLinkText("partialText"));
//        driver.findElement(By.tagName("elementTagName"));
//        driver.findElement(By.xpath("xPath"));
        
        WebElement input = driver.findElement(By.cssSelector("input[type=text]"));
        input.sendKeys("Selenium\n");
        
        Thread.sleep(5_000);
        
//        driver.close();
        driver.quit();
        
    }

}
