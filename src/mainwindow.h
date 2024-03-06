#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include "qcalendarwidget.h"
#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private:
    Ui::MainWindow *ui;
    QCalendarWidget *calendar;

};
#endif // MAINWINDOW_H
