#Εισαγωγή των απαραίτητων βιβλιοθηκών: Στις πρώτες γραμμές, εισάγουμε τις απαιτούμενες ενότητες. 
#Η SQLAlchemy εισάγεται για τον ορισμό των μοντέλων βάσης δεδομένων  
#Η datetime εισάγεται για να χειρίζεται λειτουργίες που σχετίζονται με την ημερομηνία και την ώρα

from __future__ import annotations
from sqlalchemy import String, DateTime, Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

from typing import List
from datetime import datetime

#Ορισμός βασικής κλάσης για όλες τις κλάσεις, παρέχει κοινή λειτουργικότητα και διαμόρφωση για την αντιστοίχιση αντικειμένου-σχεσιακής απεικόνισης
class Base(DeclarativeBase):
    pass

  
#Κλάση για τα στοιχεία των employees
class Employee(Base):
    __tablename__ = 'employees'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False,)
    surname: Mapped[str] = mapped_column(String(50), nullable=False)
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(15), nullable=False)
    job_position: Mapped[str] = mapped_column(String(50), nullable=False)
    date_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    
    #Διόρθωση βρόχου ανακατεύθυνσης στη διαδρομή Flask για την υποβολή αιτήσεων άδειας
    leave_requests : Mapped[List["LeaveRequest"]] = relationship("LeaveRequest", back_populates="employee")
    
    def __str__(self):
        return f"<Employee id={self.id}, name={self.name}, surname={self.surname}, birth_year={self.birth_year}, email={self.email}, phone={self.phone}, job_position={self.job_position}, date_created={self.date_created}>"
    
#Κλάση για τη δημιουργία της φόρμας αίτησης άδειας
class LeaveRequest(Base):
    __tablename__ = 'leaverequests'
    id: Mapped[int] = mapped_column(primary_key=True)    
    start_date: Mapped[Date] = mapped_column(Date)
    end_date: Mapped[Date] = mapped_column(Date)
    reason : Mapped[str] = mapped_column(String(20), nullable=False)
    status : Mapped[str] = mapped_column(String(50), default='Pending') 
    employee_id : Mapped[int] = mapped_column(ForeignKey('employees.id'))
    date_created: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.now)
    
    #Ορισμός αμφίδρομης σχέσης μεταξύ των κλάσεων Employee και LeaveRequest
    employee : Mapped[List["Employee"]] = relationship("Employee", back_populates="leave_requests")
    
    def __str__(self):
        return f"<start_date={self.start_date}, end_date={self.end_date}, reason={self.reason}, status={self.status}>"

    