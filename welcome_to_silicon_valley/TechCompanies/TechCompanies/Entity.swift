//
//  Entity.swift
//  TechCompanies
//
//  Created by Kristine Bredemeier on 5/27/16.
//  Copyright © 2016 Kristine Bredemeier. All rights reserved.
//

import Foundation

enum EntityType:String{
    case None, School, TechCompany
}

class Entity {
    private (set) var name:String = ""
    private (set) var town:String = ""
    private (set) var imageName:String = ""
    private (set) var type:EntityType = .None

    init (name:String, town:String, imageName:String, type:EntityType = .None){
        self.name = name
        self.town = town
        self.imageName = imageName
        self.type = type

    }
}