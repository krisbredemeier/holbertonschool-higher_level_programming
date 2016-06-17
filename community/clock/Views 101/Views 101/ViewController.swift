//
//  ViewController.swift
//  Views 101
//
//  Created by Kristine Bredemeier on 6/9/16.
//  Copyright © 2016 Kristine Bredemeier. All rights reserved.
//

import UIKit

class ViewController: UIViewController {


    @IBOutlet weak var viewBackground: UIView!
    @IBOutlet weak var clockLabel: UILabel!
    let clock = Clock()
    var timer: NSTimer?
    var fade: NSTimer?

//    //analog clock
//    var theTimer:NSTimer?

    override func viewDidLoad() {
        super.viewDidLoad()


        timer = NSTimer.scheduledTimerWithTimeInterval(1.0, target: self, selector: "updateTimeLabel", userInfo: nil, repeats: true)
        fade = NSTimer.scheduledTimerWithTimeInterval(5, target: self, selector: "update", userInfo: nil, repeats: true)

    }

    override func viewWillAppear(animated: Bool) {
        super.viewWillAppear(animated)
        updateTimeLabel()
    }

    func updateTimeLabel() {
        let formatter = NSDateFormatter()
        formatter.timeStyle = .MediumStyle
        clockLabel.text = formatter.stringFromDate(clock.currentTime)
    }

    func update() {
        let nextColor = getNextColor()
        UIView.animateWithDuration(5.0, animations: {
            self.view.backgroundColor = nextColor
        })
    }

        func getNextColor() -> UIColor {
            let currentColor = self.view.backgroundColor

            if currentColor == UIColor(red: 0.651, green: 0.7176, blue: 0.3216, alpha: 1.0) {
                return UIColor(red: 238/255.0, green: 238/255.0, blue: 80/255.0, alpha: 1.0)

            } else if currentColor == UIColor(red: 238/255.0, green: 238/255.0, blue: 80/255.0, alpha: 1.0) {
                return UIColor(red: 0.3294, green: 0.4863, blue: 0.4431, alpha: 1.0)
            } else if currentColor == UIColor(red: 0.3294, green: 0.4863, blue: 0.4431, alpha: 1.0) {
                return UIColor(red: 0.2549, green: 0.2431, blue: 0.3569, alpha: 1.0)
            } else if currentColor == UIColor(red: 0.2549, green: 0.2431, blue: 0.3569, alpha: 1.0) {
                return UIColor(red: 0.6784, green: 0.4588, blue: 0.6706, alpha: 1.0)
            } else {
                return UIColor(red: 0.651, green: 0.7176, blue: 0.3216, alpha: 1.0)
            }
        }

    override func supportedInterfaceOrientations() -> UIInterfaceOrientationMask {
        return UIInterfaceOrientationMask.All
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    deinit {
        if let timer = self.timer {
            timer.invalidate()
        }

////analog
//    self.setTime()
//
//    self.theTimer = NSTimer.scheduledTimerWithTimeInterval(1, target: self, selector:("setTime"), userInfo: nil, repeats: true)

    }
////analog
//func setTime(){
//
//    print("set time")
//    let date = NSDate()
//    let outputFormatter = NSDateFormatter()
//    outputFormatter.dateFormat = "hh:mm:ss"
//    let newDateString:NSString = outputFormatter.stringFromDate(date)
//    print(newDateString)
//
//    let calendar = NSCalendar.currentCalendar()
//    let components = calendar.components([.Hour, .Minute, .Second, .Nanosecond], fromDate: date)
//    var hour = components.hour
//    var minute = components.minute
//    var second = components.second
//
//    print(hour)
//    print(minute)
//    print(second)
//
//    var secAngle = (6 * second)
//    var minAngle = (6 * minute)
//    var hourAngle = (30 * hour + minute / 2)
//
//    self.secsImage.transform = CGAffineTransformMakeRotation( CGFloat(secAngle) )
//    self.minsImage.transform = CGAffineTransformMakeRotation( CGFloat(Double(minAngle)) )
//    self.hoursImage.transform = CGAffineTransformMakeRotation( CGFloat(Double(hourAngle)) )
//        
//    print(secAngle)
//    print(minAngle)
//    print(hourAngle)
//    }

}


