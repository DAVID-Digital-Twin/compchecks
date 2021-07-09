import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.*;

import javax.xml.XMLConstants;
import javax.xml.namespace.NamespaceContext;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathFactory;
 
import org.w3c.dom.Document;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;

public class Functions {

    public static String index(String path, String filename) throws Exception {
    	DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    	factory.setNamespaceAware(true);
    	DocumentBuilder builder = factory.newDocumentBuilder();
    	Document doc = builder.parse(filename);
    
        //FIXME: change xpath expression to match unique node position rather than text(), currently not working for keys with identical text()
    	String modpath = String.format("count(//*[local-name()='key'][text()='%s']/preceding-sibling::*)", path);
    	
    	//Create XPath
    	XPathFactory xpathfactory = XPathFactory.newInstance();
    	XPath xpath = xpathfactory.newXPath();
    	XPathExpression expr = xpath.compile(modpath);
              	
       	Object keys = expr.evaluate(doc, XPathConstants.NUMBER);
	
       	int i = ((Number)keys).intValue();
       	String s=String.valueOf(i);
       	return s;
    }

}