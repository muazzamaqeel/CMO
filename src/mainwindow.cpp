#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include "CalendarDelegate.h"
#include <QTableView>
#include <QKeyEvent>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow) {
    ui->setupUi(this);

    ui->CalendarBoard1->setMinimumDate(QDate(2000, 1, 1));
    ui->CalendarBoard1->setMaximumDate(QDate(2100, 1, 1));
    ui->CalendarBoard1->setGridVisible(false);
    ui->CalendarBoard1->installEventFilter(this);
    setWindowTitle(tr("CMO Calendar"));

    QList<SpecialDate> specialDates;
    specialDates.append({ QDate(2024, 12, 25), Qt::red, Qt::white, Qt::green }); // Christmas Day

    QTableView *view = ui->CalendarBoard1->findChild<QTableView *>("qt_calendar_calendarview");
    if (view) {
        CalendarDelegate *delegate = new CalendarDelegate(specialDates, this);
        view->setItemDelegate(delegate);
    }
}

bool MainWindow::eventFilter(QObject *watched, QEvent *event) {
    return false;
}

MainWindow::~MainWindow() {
    delete ui;
}
