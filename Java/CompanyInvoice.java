package org.bca.introcs.u1;
import java.util.Scanner;

public class CompanyInvoice {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		//Input
		System.out.print("Item name: ");
		String name = scan.nextLine();
		System.out.print("Quantity Purchased: ");
		int quantity = scan.nextInt();
		System.out.print("Price per Item: ");
		float price = scan.nextFloat();
		// 2nd Input
		System.out.print("2nd Item's name: ");
		scan.nextLine();
		String name2 = scan.nextLine();
		System.out.print("Quantity Purchased: ");
		int quantity2 = scan.nextInt();
		System.out.print("Price per Item: ");
		float price2 = scan.nextFloat();
		
		float total = quantity * price;
		float total2 = quantity2 * price2;
		float absolutetotal = total + total2;
		
		System.out.printf("\n%10s %10s %15s %10s\n", "Item Name", "Count", "Unit Cost", "Total");
		System.out.printf("%10s %10d %15.2f %10.2f\n", name, quantity, price, total);
		System.out.printf("%10s %10d %15.2f %10.2f\n\n", name2, quantity2, price2, total2);
		System.out.printf("%10s %36.2f", "Grand total", absolutetotal);
		
		
		
		
	}

}
