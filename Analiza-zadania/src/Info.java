import java.io.*;
import java.util.ArrayList;

import org.jsoup.*;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Info {

    //Define StringBuilder to keep created sites
    private StringBuilder site = new StringBuilder();
    private StringBuilder newsletter = new StringBuilder();
    private ArrayList<String> addresses = new ArrayList<>();

    public String information(String phrase){
        addresses.add("https://wp.pl");
        addresses.add("https://tvn24.pl");
        addresses.add("https://gov.pl");
        try{
            for (String url: addresses) {
                //Connect to URL address
                Connection connect = Jsoup.connect(url);
                //Start each block with URL address of the currently browsed www site
                site.append("<h1>").append(url).append("</h1>");
                //Get www site as Document object
                Document document = connect.get();
                //Find all <a> tags
                //TODO 1.1 Znajdź w documencie wszystkie znaczniki <a ...>, zapisz je jako allA
                //Search through all found <a> tags
                for (Element elem : allA) {
                    //Compare given phrase with text from Elements
                    if () { //TODO 1.1 Znajdź w tekście wszystkie wystąpienia phrase (przydatna może okazac się funkcja text())
                        //Handle relative addresses
                        if (elem.attr("href").startsWith("/")) {
                            //TODO 1.1 Utwórz hiperłącze na wyszukanym tekście, który umieścisz jako h2. Warto opakować hiperłącza w containery

                        } else {
                            //TODO 1.1 Witryna gov.pl nie jest skora do współpracy. Dodaj adres url do znacznika <a href> przed przypisaniem adresu, pod którym znajduje się artykuł

                        }
                    }
                }
            }
        }catch (IOException e){
            System.err.println(e);
        }
        return site.toString();
    }

    public String newsToNewsletter(){
        addresses.add("https://wp.pl");
        addresses.add("https://tvn24.pl");
        addresses.add("https://gov.pl");
        try{
            newsletter.append("Najświeższe informacje o koronawirusie:");
            for (String url: addresses) {
                //Connect to URL address
                Connection connect = Jsoup.connect(url);
                //Start each block with URL address of the currently browsed www site
                newsletter.append("\n\nZe strony: " + url+":");
                //Get www site as Document object
                Document document = connect.get();
                //Find all <a> tags
                //TODO 1.1 Znajdź w documencie wszystkie znaczniki <a ...>, zapisz je jako allA
                //Search through all found <a> tags
                for (Element elem : allA) {
                    //Compare given phrase with text from Elements
                    if () { //TODO 1.1 Znajdź w tekście wszystkie wystąpienia 'koronawirus' (przydatna może okazac się funkcja text())
                        if (elem.attr("href").startsWith("/")) {
                            //TODO 1.1 Dopisz adres URL jeśli strona zawiera adresowanie względne, a następnie zapisz tytuł
                            //TODO 1.1 artykułu i odnośnik do niego do zmiennej newsletter
                        } else {
                            //TODO 1.1 Dopisz tytuł artykułu i odnośnik do niego do zmiennej newsletter
                        }
                    }
                }
            }
        }catch (IOException e){
            System.err.println(e);
        }
        return newsletter.toString();
    }
}
