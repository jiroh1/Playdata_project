package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

import Entity.EmpEntity;
import static myjdbc.JDBCTemplate.*;

//CRUD�� �ϰڴ�. = commit/rollback 
public class EmpDao implements EmpDaoIm{
	Connection con;
	public EmpDao(Connection con) {
		this.con = con;
	}




	//1. select
	public List<EmpEntity> getselectAll(){
		String all = "select * from join";
		//���ڵ� ���پ� EmpEntity �� ��Ƽ� list��ü�� �߰��� ���� ����
		List<EmpEntity> Listall = new ArrayList<>();
		EmpEntity entity = null;
		Statement stmt = null;
		ResultSet rs = null; //db���� �������ִ� �޼���? result -> entity�� �־ �����Ұ��̴�
		
		try {
			 stmt = con.createStatement();
			 rs = stmt.executeQuery(select_all);
			 while(rs.next()) {
				 entity = new EmpEntity(rs.getString(1), 
						  rs.getString(2),
						  rs.getString(3),
						  rs.getString(4));
				 
				 Listall.add(entity); //list �߰��Ѵ� ���྿!
			 }//while add
			 
		}catch(Exception e) {
				
		
	} finally {
		Close(rs);
		Close(stmt);
	}//try end
		return Listall; // return�ϸ� jdbctemplate�ΰ���
	}

	//2. insert
	public int getEmpInsert(EmpEntity entity) {

		PreparedStatement pstm = null; // value ���� ���� �����Ҷ� (?,?,?,?)
		int res =0; //insert input 1, out0 �׷��� int�� �ؾ��Ѵ�.
		try {
			pstm = con.prepareStatement(insert_emp);
			pstm.setString(1, entity.getId()); //ù��°����ǥ 1
			pstm.setString(2, entity.getPw());
			pstm.setString(3, entity.getEml());
			pstm.setString(4, entity.getTel());


			res = pstm.executeUpdate(); // insert ����
			if (res >0) { // ������ 1, ������ 0 �̱� ������ ���� commit!
				Commit(con);
			}
		}catch(Exception e) {
			//System.out.println(e.toString());
			Rollback(con);
		}finally {
			Close(pstm);
		}
		return res;
	}}
	
	
	
//	// update, delete �ʿ���� 	
//	//3. update
//	public int getEmpUpdate(EmpEntity entity) {
//
//		PreparedStatement pstm = null;
//		int res =0;
//		try {
//			pstm = con.prepareStatement(update_emp);
//			pstm.setDouble(1, entity.getSal());
//			pstm.setInt(2, entity.getEmpno());
//
//			
//			res = pstm.executeUpdate(); // insert ����
//			if (res >0) {
//				Commit(con);
//			}
//		}catch(Exception e) {
//			//System.out.println(e.toString());
//			Rollback(con);
//		}finally {
//			Close(pstm);
//		}
//		return res;
//	}
//	
//	
//	
//	//4. delete
//	public int getEmpDelete(EmpEntity entity) {
//
//		PreparedStatement pstm = null;
//		int res =0;
//		try {
//			pstm = con.prepareStatement(delect_emp);
//			
//			pstm.setInt(1, entity.getEmpno());
//
//			
//			res = pstm.executeUpdate(); // insert ����
//			if (res >0) {
//				Commit(con);
//			}
//		}catch(Exception e) {
//			
//			Rollback(con);
//		}finally {
//			Close(pstm);
//		}
//		return res;
//	}
//	}
