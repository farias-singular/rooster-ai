```csharp
namespace Project.Tests.Domain.Brands
{
    public class BrandTest
    {
        private readonly IBrandUniquenessChecker _brandUniquenessChecker = Substitute.For<IBrandUniquenessChecker>();

        [Fact]
        public void CheckBrokenRuleIdNotUnique()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(false);

            // Act & Assert
            var ex = Assert.Throws<BusinessRuleValidationException>(
                () => Brand.Create(
                    id: "brand",
                    organization: organization,
                    category: category,
                    name: "name",
                    title: "title",
                    brandUniquenessChecker: _brandUniquenessChecker));

            Assert.Equal("Brand is not unique or is invalid.", ex.Details);
        }

        [Fact]
        public void BrandCreatedEventIsDispatched()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            // Act
            var brand = Brand.Create(
                id: "brand",
                organization: organization,
                category: category,
                name: "name",
                title: "title",
                brandUniquenessChecker: _brandUniquenessChecker);

            // Assert
            var domainEvent = brand.DomainEvents.OfType<BrandCreatedEvent>().FirstOrDefault();
            Assert.NotNull(domainEvent);
            Assert.Equal(brand, domainEvent.Brand);
        }

        [Fact]
        public void BrandUpdatedEventIsDispatchedWhenNameIsUpdated()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            var brand = Brand.Create(
                id: "brand",
                organization: organization,
                category: category,
                name: "name",
                title: "title",
                brandUniquenessChecker: _brandUniquenessChecker);

            // Act
            brand.SetName("new name");
            brand.SaveChanges();

            // Assert
            var domainEvent = brand.DomainEvents.OfType<BrandUpdatedEvent>().FirstOrDefault();
            Assert.NotNull(domainEvent);
            Assert.Equal(brand, domainEvent.Brand);
        }

        [Fact]
        public void BrandUpdatedEventIsDispatchedWhenTitleIsUpdated()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            var brand = Brand.Create(
                id: "brand",
                organization: organization,
                category: category,
                name: "name",
                title: "title",
                brandUniquenessChecker: _brandUniquenessChecker);

            // Act
            brand.SetTitle("new title");
            brand.SaveChanges();

            // Assert
            var domainEvent = brand.DomainEvents.OfType<BrandUpdatedEvent>().FirstOrDefault();
            Assert.NotNull(domainEvent);
            Assert.Equal(brand, domainEvent.Brand);
        }

        [Fact]
        public void BrandDeletedEventIsDispatched()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            var brand = Brand.Create(
                id: "brand",
                organization: organization,
                category: category,
                name: "name",
                title: "title",
                brandUniquenessChecker: _brandUniquenessChecker);

            // Act
            brand.Delete();

            // Assert
            var domainEvent = brand.DomainEvents.OfType<BrandDeletedEvent>().FirstOrDefault();
            Assert.NotNull(domainEvent);
            Assert.Equal(brand, domainEvent.Brand);
        }

        [Fact]
        public void CheckBrokenRuleNameMustNotBeEmpty()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            // Act & Assert
            var ex = Assert.Throws<BusinessRuleValidationException>(
                () => Brand.Create(
                    id: "brand",
                    organization: organization,
                    category: category,
                    name: "",
                    title: "title",
                    brandUniquenessChecker: _brandUniquenessChecker));

            Assert.Equal("Name must not be empty.", ex.Details);
        }

        [Fact]
        public void CheckBrokenRuleTitleMustNotBeEmptyWhenNotNull()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            // Act & Assert
            var ex = Assert.Throws<BusinessRuleValidationException>(
                () => Brand.Create(
                    id: "brand",
                    organization: organization,
                    category: category,
                    name: "name",
                    title: "",
                    brandUniquenessChecker: _brandUniquenessChecker));

            Assert.Equal("Title must not be empty.", ex.Details);
        }

        [Fact]
        public void SetNameUpdatesBrandAndDispatchedEvent()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            var brand = Brand.Create(
                id: "brand",
                organization: organization,
                category: category,
                name: "name",
                title: "title",
                brandUniquenessChecker: _brandUniquenessChecker);

            // Act
            brand.SetName("updated name");
            brand.SaveChanges();

            // Assert
            Assert.Equal("updated name", brand.Name);
            var domainEvent = brand.DomainEvents.OfType<BrandUpdatedEvent>().FirstOrDefault();
            Assert.NotNull(domainEvent);
            Assert.Equal(brand, domainEvent.Brand);
        }

        [Fact]
        public void SetTitleUpdatesBrandAndDispatchedEvent()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            var brand = Brand.Create(
                id: "brand",
                organization: organization,
                category: category,
                name: "name",
                title: "title",
                brandUniquenessChecker: _brandUniquenessChecker);

            // Act
            brand.SetTitle("updated title");
            brand.SaveChanges();

            // Assert
            Assert.Equal("updated title", brand.Title);
            var domainEvent = brand.DomainEvents.OfType<BrandUpdatedEvent>().FirstOrDefault();
            Assert.NotNull(domainEvent);
            Assert.Equal(brand, domainEvent.Brand);
        }

        [Fact]
        public void CheckBrokenRuleNameMustNotBeEmptyWhenSettingName()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            var brand = Brand.Create(
                id: "brand",
                organization: organization,
                category: category,
                name: "name",
                title: "title",
                brandUniquenessChecker: _brandUniquenessChecker);

            // Act & Assert
            var ex = Assert.Throws<BusinessRuleValidationException>(
                () => brand.SetName(""));

            Assert.Equal("Name must not be empty.", ex.Details);
        }

        [Fact]
        public void CheckBrokenRuleTitleMustNotBeEmptyWhenSettingTitle()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();

            _brandUniquenessChecker.IsUnique("brand", organization.Id).Returns(true);

            var brand = Brand.Create(
                id: "brand",
                organization: organization,
                category: category,
                name: "name",
                title: "title",
                brandUniquenessChecker: _brandUniquenessChecker);

            // Act & Assert
            var ex = Assert.Throws<BusinessRuleValidationException>(
                () => brand.SetTitle(""));

            Assert.Equal("Title must not be empty.", ex.Details);
        }
    }
}
```