package j.ucdavis22.w2;

/*
 * Jörn Boehnke 2022
 */

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.nio.charset.StandardCharsets;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

public class AmazonDeal {
    
    public static void main(String[] args) throws IOException {
        
        Document doc = Jsoup.connect("https://www.amazon.com/dp/B07Q6ZWMLR") // https://www.amazon.com/dp/B07Q32KX3J
                            .userAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36")
                            .get();
        
//        System.out.println(doc.html());
        
        Elements timers = doc.select("span[id^=deal_expiry_timer]");
        System.out.println(timers.text());
        
//        saveString(new File("B07Q32KX3J.htm"), doc.html(), false);
        
    }
    
    public static boolean saveString(File f, String s, boolean append) throws IOException {
        try (
            FileOutputStream fos = new FileOutputStream(f, append);
            OutputStreamWriter osw = new OutputStreamWriter(fos, StandardCharsets.UTF_8);
            BufferedWriter bw = new BufferedWriter(osw);
        ) {
            bw.write(s);
            bw.flush();
            return true;
        }
    }
    
}
