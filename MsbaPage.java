package j.ucdavis22.w2;

/*
 * Jörn Boehnke 2022
 */

import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

public class MsbaPage {
    
    public static void main(String[] args) {
        
        try {
            
            /*
             * connects to the server and download its HTML page
             */
            Document doc = Jsoup.connect("https://gsm.ucdavis.edu/master-science-business-analytics-msba")
                                .userAgent("Mozilla/5.0") // optional here, but may be required elsewhere
                                .get();
            
            /*
             * selects "<p>" that immediately follows "<div>" of class "col-md-6"
             */
            Elements ps = doc.select("div.col-md-6 > p");
            
            /*
             * prints the HTML content to the screen (almost only text here;
             * just need to replaces "&nbsp;" with " ")
             */
            System.out.println(ps.first().html().replace("&nbsp;", " "));
            
        } catch ( IOException ex ) {
            
            System.out.println("Problem with the connection...");
            
        }
        
    }
    
}
