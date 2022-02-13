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

public class Vivino {

    public static void main(String[] args) throws InterruptedException {
        
        WebDriverManager.chromedriver().setup();
        WebDriver driver = new ChromeDriver();
        
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(20));
        driver.manage().timeouts().scriptTimeout(Duration.ofMinutes(4));
        driver.manage().timeouts().pageLoadTimeout(Duration.ofSeconds(20));
        
        driver.get("https://www.vivino.com/");
        
        Thread.sleep(2_000);
        
        WebElement wines = driver.findElement(By.cssSelector("span[title='Wines']"));
        wines.click();
        
        Thread.sleep(2_000);
        
        WebElement white = driver.findElement(By.xpath("//span[text()='White']"));
        white.click();
        
        Thread.sleep(2_000);
        
        WebElement sparkling = driver.findElement(By.xpath("//span[text()='Sparkling']"));
        sparkling.click();
        
        Thread.sleep(5_000);
        
//        driver.close();
        driver.quit();
        
    }

}
