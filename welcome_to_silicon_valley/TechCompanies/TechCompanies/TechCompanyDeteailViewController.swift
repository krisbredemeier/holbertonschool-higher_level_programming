//  TechCompaniesListViewController.swift
//  TechCompanies
//
//  Created by Kristine Bredemeier on 5/27/16.
//  Copyright © 2016 Kristine Bredemeier. All rights reserved.
//

import UIKit

class DeteailsViewController: UIViewController {

    // connect lable and image

    
    var schoolList:[Entity]!
    var techCompanyList:[Entity]!

    

    //var label = UILabel(frame: CGectMake(10, 10, 200, 21))
    //    self.view.addSubView(label)

    override func viewDidLoad() {
        super.viewDidLoad()

        techCompanyList = EntitiesHelper.getTechCompanies()
        schoolList = EntitiesHelper.getSchools()

//        if self.entity != nil {
//
//            self.title = Entity.name
//            self.lblEntity.text = Entity.town
//            self.imgEntity.image = UIImage(imageLiteral: entity.imageName)
//        }


        // Do any additional setup after loading the view.
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    


    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepareForSegue(segue: UIStoryboardSegue, sender: AnyObject?) {
        // Get the new view controller using segue.destinationViewController.
        // Pass the selected object to the new view controller.

        if segue.identifier == "techSg" {
            let destVC = segue.destinationViewController as? DeteailsViewController

            let sectionSelected = tableView.indexPathForSelectedRow.section

            let rowSeleccted = tableView.indexPathForSelectedRow?.row

            let list = sectionSelected == 0 ?techCompanyList : schoolList

                destVC?.entity = list[rowSeleccted!]
        }

    }
    func numberOfSectionsInTableView(tableView: UITableView) -> Int {

    }
    func tableView(tableView: UITableView, numberOfRowsInSection section: Int) -> Int {

    }

    func tableView(tableView: UITableView, titleForHeaderInSection section: Int) -> String? {

    }

    func tableView(tableView: UITableView, cellForRowAtIndexPath indexPath: NSIndexPath) -> UITableViewCell {
        
    }


}
