package Main;
import java.util.Scanner;

public class Main {
	static int w[] = {1,2,3,4,5,6,7,8,9,10};
	static int target;
	static int x[] = new int[10];
	public static void main(String[] args) {	
		int total=0;
		Scanner sc = new Scanner(System.in);
		System.out.println("검사할 숫자 입력:");
		target = sc.nextInt();
		for (int i=0;i<w.length;i++) {
			total += w[i];
		}
		sum_subset(-1,0,total);
	}
	public static void sum_subset(int i,int weight,int total) {
		if (target==weight) {
			print();
		}
		else {
			if (i<w.length-1 && weight + w[i + 1] <= total) { //다음 수를 담아도 total 이하면 진행
				x[i+1] = w[i+1]; //다음 수 담기
				sum_subset(i+1,weight + w[i+1],total); // 담은 상태로 진행
				x[i+1] = 0; // 담은 수를 0으로 초기화하고
				sum_subset(i+1,weight,total); // i+1번째 수를 담지 않은 상태로 진행
			}
			
		}
	}
	public static void print() {
		for(int i=0;i<x.length;i++) {
			if(x[i]!=0) {
				System.out.print(x[i]+" ");
			}
		}
		System.out.println();
	}
}
