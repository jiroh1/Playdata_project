package myjdbc;

import Entity.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.*;


 // �Ź� db�ڵ� ����ݱ� ����ϱ� �ϳ� ����� ����.
 // �ϳ��� ���̺�� �ϳ��� ���ø� (ex, �ϳ��� emp table�� �ϳ��� ���ø�)
 // Emp -> Entity / CRUD -> static
 //	Emp -> VO
 // ��� db�� static -> �ѹ��� insert�ϰԲ�, ���� static�̾�߸� ������� �ȴ�. ������ �Ҹ���������� static���� �Ѵ�.
 // Emp -> db������ ��üȭ �������� Entity ��� �θ���. (���̺��� ��üȭ �Ǿ��ִ°� ��ƼƼ��� �θ���)
 // ���� CRUD�� ����־�߾� �Ѵ�. CRUD -> static


// ����, Ŭ���� = Connection 
// �ѹ�, Ŀ�Ը� �ϰڴ�.  = Statement


public class JDBCTemplate {
	
	public static Connection getConnection() {
		Connection con = null;
		
		//1. ����	
		try {
			Class.forName("oracle.jdbc.driver.OracleDriver");
			con = DriverManager.getConnection("jdbc:oracle:thin:@127.0.0.1:1521:XE","scott","TIGER");
		if(!con.isClosed()) {
			System.out.println("�����߾� ");
		}
		
		} catch (ClassNotFoundException | SQLException e) {
			e.printStackTrace();
		}
		return con;
	}
	public static void Close(Connection con) {
		if(con != null) {
			try {
				con.close();
			}catch(SQLException e) {
				e.printStackTrace();
			}
		}
	}
	
	
	public static void Close(Statement stmt) {
		if(stmt != null) {
			try {
				stmt.close();
			}catch(SQLException e) {
				e.printStackTrace();
			}
		}
	}
	
	public static void Close(ResultSet rs) {
		if (rs != null) {
			try {
				rs.close();
			}catch (SQLException e) {
				e.printStackTrace();
			}
		}
		}
	
	
	public static void Rollback(Connection con) {
		if(con != null) {
			try {
				con.rollback();
			} catch (SQLException e) {
				
				e.printStackTrace();
			}
		}
	}
	public static void Commit(Connection con) {
		if(con != null) {
			try {
				con.commit();
			} catch (SQLException e) {
				
				e.printStackTrace();
			}
		}
	}	
	public static boolean isConnection(Connection con) {
		try {
			if(con != null && !con.isClosed()) { 
				// &��Ʈ����, (a>b)&&(a<b++) ������ -> ���� ����� false �� �ڿ� ���� ������ϰ� ����� false�� ����
				// (a>b)||(a<b++)  -> ���� ����� true �� �ڿ� ���� ������ϰ� ����� true�� ����
				return true;
			}
		} catch (SQLException e) {
			
			e.printStackTrace();
		}
		return false;
	}
}
