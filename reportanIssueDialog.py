from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QDialogButtonBox

class ReportIssueDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Report an Issue")
        
        layout = QVBoxLayout()

        issue_text = """
        If you encounter any issues or need support, please contact the following:

        1. Justin Omare Ratemo (Senior Developer)
           - Phone: 0793031269
           - Email: justopizo01@gmail.com

        2. Amos Kilonzo (Senior GUI Developer)
           - Phone: 0712343212

        We will respond to your query as soon as possible. Thank you for using the system!
        """
        
        issue_label = QLabel(issue_text)
        layout.addWidget(issue_label)
        
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        layout.addWidget(button_box)
        
        self.setLayout(layout)
        self.resize(500, 400) 
        self.setMinimumSize(400, 300) 
